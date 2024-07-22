
import WSCommits 
import markdown
from toMarkdownFromWS import ToMarkdown 

def show_menu():
    print("1. Obtener Commits De GitHub")
    print("2. Salir")

def enter_value():
    valor = input("Ingresa el link de github: ")
    return valor


def main():
    while True:
        show_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            url = enter_value()
            ws = WSCommits.WSCommits(url)
            commits = ws.fetch_commits()
            text = ToMarkdown(commits).to_markdown()
            html = markdown.markdown(text, extensions=['tables'])
            
            # Abre un archivo en modo de escritura. Si el archivo no existe, se crea.
            with open('commits.txt', 'w') as file:
                file.write('|Repository|Branch|Commit Id|Commit Message|Commit Message Body|Commited on (Date)|\n')
                file.write('|----------|------|---------|--------------|-------------------|------------------|\n')
                for commit in commits:
                    file.write('|'+ commit.repository + '|' + commit.branch + '|' + commit.commit_id + '|' + commit.message+ '|' + commit.message +'|----|' +'\n')
            with open('commits2.txt', 'w') as file:
                file.write(html)  # Escribe el contenido HTML en el archivo.

            print("Contenido guardado en output.txt")

        elif opcion == '2':
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()