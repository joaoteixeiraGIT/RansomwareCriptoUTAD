# RansomwareCriptoUTAD

# ⚠️ Aviso ⚠️
Este projeto é uma simulação de um ataque de ransomware criado para fins educacionais e de conscientização sobre segurança. Ele encripta arquivos na diretoria "Documents" do utilizador e exibe uma interface gráfica informando sobre a criptografia, seguida por uma opção de desencriptar os arquivos. 
Não deve ser utilizado para qualquer finalidade maliciosa ou ilegal. Utilize-o somente em um ambiente Linux controlado e com a devida autorização. 

# Arquivos Principais
- gui.py: Interface gráfica do usuário (GUI) que inicia a criptografia e oferece a opção de desencriptação.
- ransomware.py: Lida com a criptografia dos arquivos. Encripta todos os arquivos na diretoria "Documents" do utilizador e altera as permissões para somente leitura. 
- decryptor.py: Lida com a desencriptação dos arquivo. Restaura os arquivos para o estado original, alterando as permissões para edição. 

# Requisitos
- Python 3.x
- tkinter
- cryptography


  




