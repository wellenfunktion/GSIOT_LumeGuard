import cv2
import mediapipe as mp
import winsound
import collections
import datetime

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

video_path = "teste_aceno_escuro.mp4"

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ Erro ao abrir o vídeo.")
    exit()
print("Vídeo aberto com sucesso. Iniciando detecção de mãos...")

def log_event(mensagem):
    with open("log_lumeguard.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {mensagem}\n")

def dedos_levantados(hand_landmarks):
    # Lista dos pontos das pontas dos dedos: [polegar, indicador, medio, anelar, minimo]
    tips_ids = [4, 8, 12, 16, 20]
    dedos = []

    # Polegar: verifica se está aberto para ambos os lados (palma ou dorso)
    polegar_tip = hand_landmarks.landmark[tips_ids[0]]
    polegar_base = hand_landmarks.landmark[tips_ids[0] - 1]
    
    if abs(polegar_tip.x - polegar_base.x) > 0.05:
        dedos.append(1)
    else:
        dedos.append(0)

    # Restante dos dedos (vertical)
    for id in range(1, 5):
        if hand_landmarks.landmark[tips_ids[id]].y < hand_landmarks.landmark[tips_ids[id] - 2].y:
            dedos.append(1)
        else:
            dedos.append(0)
    return dedos  # [polegar, indicador, medio, anelar, minimo]

beep_ativo = False  # Controle para evitar múltiplos beeps do sinal de paz
beep_aceno_ativo = False  # Controle para evitar múltiplos beeps do aceno

# Para detectar movimento lateral (aceno)
centros_mao = collections.deque(maxlen=10)  # Guarda os últimos centros da mão

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    aceno_detectado = False

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            dedos = dedos_levantados(hand_landmarks)

            # Calcula o centro da mão (média dos pontos)
            xs = [lm.x for lm in hand_landmarks.landmark]
            ys = [lm.y for lm in hand_landmarks.landmark]
            centro_x = sum(xs) / len(xs)
            centro_y = sum(ys) / len(ys)
            centros_mao.append(centro_x)

            if dedos.count(1) >= 4:
                if len(centros_mao) == centros_mao.maxlen:
                    movimento = max(centros_mao) - min(centros_mao)
                    if movimento > 0.10:  # ajuste esse valor conforme necessário
                        aceno_detectado = True

            if aceno_detectado:
                if not beep_aceno_ativo:
                    print("👋 ACENO DETECTADO! SINAL DE EMERGÊNCIA")
                    winsound.Beep(800, 800)
                    beep_aceno_ativo = True
                    log_event("ACENO DETECTADO! SINAL DE EMERGÊNCIA")
                cv2.putText(frame, "ACENO DETECTADO!", (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (174, 174, 185), 2)
            else:
                beep_aceno_ativo = False

            if dedos == [0, 1, 1, 0, 0]:
                if not beep_ativo:
                    print("⚠️ EMERGÊNCIA: Sinal de paz detectado! Usuário precisa de ajuda.")
                    winsound.Beep(1000, 200)
                    beep_ativo = True
                    log_event("SINAL DE PAZ DETECTADO! Usuário precisa de ajuda.")
                cv2.putText(frame, "Sinal detectado! Usuário precisa de ajuda.", (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            else:
                beep_ativo = False
                cv2.putText(frame, "Mao detectada", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        beep_ativo = False
        beep_aceno_ativo = False
        cv2.putText(frame, "Nenhuma mao detectada", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Hand Detector - LumeGuard', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Detecção de mãos finalizada. Fechando o vídeo.")