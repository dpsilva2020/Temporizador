import time
import pyautogui
import subprocess


# Defina o tempo em segundos sem movimento do mouse para mostrar a mensagem
tempo_sem_movimento = 10  # 300 segundos = 5 minutos
caminho_do_bat = 'C:\\Temporizador\\Logoff.bat'

ultima_posicao = pyautogui.position()

while True:
    time.sleep(10)  # Verifique a cada 10 segundos

    nova_posicao = pyautogui.position()

    if nova_posicao == ultima_posicao:
        # Abre uma mensagem se não houver movimento do mouse
       # print("Você está inativo!")
          # Substitua pelo URL da página que você deseja fechar
      
   
           print("Você está inativo!") 
           try:
              subprocess.run(caminho_do_bat, shell=True)
           except subprocess.CalledProcessError as e:
              print(f"Erro ao executar o arquivo .bat: {e}")
        # Substitua o print pela lógica para abrir uma mensagem na tela
    else:
        ultima_posicao = nova_posicao
