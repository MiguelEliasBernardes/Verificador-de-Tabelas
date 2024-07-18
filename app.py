import flet as ft
import verifica
import time


def main(page: ft.Page):
    
    def liga():
        valor_nome = nome_tabela.value
        valores_pesquisa = pesquisa.value
        
        return {"valor_nome":valor_nome,
                "valores_pesquisa":valores_pesquisa
                }

    
    def imprime_dados(e):
        
        try:
            valor_nome = nome_tabela.value
           
            if(valor_nome == ''):
                nome_tabela.label = "Digite uma Tabela"
                nome_tabela.border_color = 'red'
                nome_tabela.update()
                
                time.sleep(5)
                
                nome_tabela.label = "Nome Tabela"
                nome_tabela.border_color = 'blue'
                nome_tabela.update()
                
            else:
                
                page.remove(centralizar_verticalmente)
                
                data = verifica.verifica_despesa()
                dados = verifica.ajusta_lista(data["array"])
                
                controls = ft.Column(
                    controls=[nome_tabela, pesquisa, enviar_dados],
                    spacing=30,
                )
                
                scroll_container = ft.Column(
                    scroll='auto', 
                    width=500, 
                    height=500,
                    expand=False,
                )
    
                scroll_container.controls.append(ft.Text(dados,size=17))

                texto_total = ft.Text(
                    f"{data['total']}",
                    width=500,
                    height=100,
                    size=30,
                    color='blue'
                )

                page_layout = ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                controls,
                                scroll_container,
                            ],
                            alignment="start",
                            spacing=50,
                        ),
                        ft.Row(
                            controls=[texto_total],
                            alignment="end",
                            spacing=40,
                        )
                    ],
                    alignment="start",
                    spacing=20,
                )
                            
                page.add(page_layout)
                page.update()
            
        except():
            pass
        
     
    
    page.title = "Verifica Tabelas"
    page.theme_mode = ft.ThemeMode.DARK
    
    page.padding = 50
    page.window_width = 1024
    page.window_height = 700
    page.window_center()

    
    
    nome_tabela = ft.TextField(
        label="Nome Tabela",
        width=300,
        border_color='blue',
        border_width=3)
    
    
    
    pesquisa = ft.TextField(label="Digite o que deseja pesquisar!",
                            width=300,
                            border_color='blue',
                            border_width=3)
    
    
    enviar_dados = ft.ElevatedButton("Fazer pesquisa",
                                     on_click=imprime_dados,
                                     width=300,
                                     bgcolor='blue',
                                     color='white')
    
    
    centralizar_verticalmente = ft.Column(
        [
            nome_tabela,
            pesquisa,
            enviar_dados
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        height=500,
        spacing=30
        
    )

    page.add(centralizar_verticalmente)

    page.update()

ft.app(target=main)