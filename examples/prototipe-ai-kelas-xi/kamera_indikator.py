"""Classroom baseline: eye visibility indicator, not a drowsiness classifier."""
import time
import cv2

face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml")
if face.empty() or eye.empty():
    raise RuntimeError("Model cascade tidak tersedia")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap.release()
    raise RuntimeError("Kamera tidak terbuka; cek izin dan indeks")
mulai = None
try:
    while True:
        ok, frame = cap.read()
        if not ok:
            print("Frame gagal; pemeriksaan berhenti")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.1, 5, minSize=(80, 80))
        status = "TIDAK DAPAT DINILAI"
        if len(faces) == 1:
            x, y, w, h = faces[0]
            roi = gray[y:y + int(h * 0.6), x:x + w]
            eyes = eye.detectMultiScale(roi, 1.1, 5, minSize=(15, 15))
            if len(eyes) >= 2:
                mulai = None
                status = "MATA TERDETEKSI"
            else:
                if mulai is None:
                    mulai = time.monotonic()
                durasi = time.monotonic() - mulai
                status = f"MATA KURANG TERDETEKSI {durasi:.1f}s"
                if durasi >= 2.0:
                    status = "PERIKSA VISIBILITAS MATA"
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            mulai = None
        cv2.putText(frame, status, (15, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 255), 2)
        cv2.imshow("Prototipe kelas - tekan q untuk keluar", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
