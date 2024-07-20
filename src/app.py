import flet as ft
import verifica as verifica
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 
from reportlab.fonts import *
import getpass
import os


def main(page: ft.Page):
    user_windows = getpass.getuser()

    if os.path.exists(f"C:\\Users\\{user_windows}\\Desktop\\PDF") == False or os.path.exists(f"C:\\Users\\{user_windows}\\Desktop\\TABELAS") == False:
        os.makedirs(f"C:\\Users\\{user_windows}\\Desktop\\PDF")
        os.makedirs(f"C:\\Users\\{user_windows}\\Desktop\\TABELAS")

    def salvar_pdf(mes,ano,pesquisa):

        def posicao():
            
            pos = 740
            var = 0
            primeira_pagina = True
            for itens in data['array']:
                if pos < 40: 
                    cnv.showPage() 
                    pos = 800  
                    
                    if primeira_pagina:
                        primeira_pagina = False
                    else:
                        cnv.setFont('Helvetica-Oblique', 12)

                cnv.setFont('Helvetica-Oblique', 12)
                cnv.drawString(30, pos, f'{itens["nome_dado"]}')
                cnv.drawString(480, pos, f'{itens["valor_dado"]}')
                pos -= 20
                var = pos
            return var
        
        try:
            data = verifica.verifica_despesa(mes,ano, pesquisa)
            dados = verifica.ajusta_lista(data["array"])
            
            
            nome_pesquisa = ''
            for i in pesquisa:
                if i == ' ':
                    nome_pesquisa += "-"
                else:
                    nome_pesquisa += i

            caminho_pasta = f"C:\\Users\\{user_windows}\\Desktop\\PDF"
            if not os.path.exists(caminho_pasta):
                os.makedirs(caminho_pasta)
            caminho_pdf = os.path.join(caminho_pasta, f"{nome_pesquisa}--{mes}.pdf")
        
            cnv = canvas.Canvas(caminho_pdf, pagesize=A4)
            cnv.setFont('Helvetica-Oblique',18)
            cnv.drawString(200,800,f"MÊS: {mes} - {ano}")
            cnv.line(20, 780, 565,780)
            
            pos = posicao()
            
            cnv.line(20, pos, 565,pos)
            cnv.setFont('Helvetica-Oblique',28)
            cnv.drawString(30,pos - 40, f'TOTAL: ')  
            cnv.drawString(370,pos - 40, f'R$ {data['total']}')

            cnv.showPage()
            cnv.save()
        except(FileNotFoundError):
            dlg_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text("ERRO AO GERAR PDF"),
                actions_alignment=ft.MainAxisAlignment.END
            )

            page.add(dlg_modal)
            page.update()

    
    
    def att(data):
                
        dados = verifica.ajusta_lista(data["array"])
        
        controls = ft.Column(
            controls=[nome_tabela,ano, pesquisa, enviar_dados,salva],
            spacing=30,
            )
                    
        scroll_container = ft.Column(
            scroll='auto', 
            width=500, 
            height=500,
            expand=False,
        )

        if data["total"] == "TOTAL = R$ 0":
                scroll_container.controls.append(ft.Text("Nenhum dado com esse nome!",size=25))
                
                texto_total = ft.Text(
                    f"R$ {data['total']}",
                    width=500,
                    height=100,
                    size=30,
                    color='blue'
                )
            
                page.controls.clear()

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
        
        else:
            scroll_container.controls.append(ft.Text(dados,size=17))
            
            texto_total = ft.Text(
                f"MÊS: {nome_tabela.value} - R$ {data['total']}",
                width=550,
                height=100,
                size=30,
                color='blue'
            )
           
            page.controls.clear()

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
        

    def erro_nome():
        nome_tabela.label = "Digite uma Tabela"
        nome_tabela.border_color = 'red'
        nome_tabela.update()
                
        time.sleep(5)
                
        nome_tabela.label = "Nome Tabela"
        nome_tabela.border_color = 'blue'
        nome_tabela.update()
    
    
    def cria_scroll(data):

        try:
            page.remove(centralizar_verticalmente)
            #print("ent")
            att(data)
            
        except(ValueError):
            #print('sai')
            att(data)


    def imprime_dados():
        
        try:
            valor_nome = nome_tabela.value
            valor_ano = ano.value
            valor_pesquisa = pesquisa.value
            
            if(valor_nome == ''):
                erro_nome()
                
            else:
                
                try:
                    data = verifica.verifica_despesa(valor_nome, valor_ano, valor_pesquisa)

                    if data == FileNotFoundError:
                        erro_nome()

                    else:
                        cria_scroll(data)
                except(FileNotFoundError):
                    erro_nome()
        
        
        except(ValueError):
            erro_nome()
    
    
    page.title = "Verifica Tabelas"
    page.theme_mode = ft.ThemeMode.DARK
    
    page.window_icon = 'tabela2.ico'
    page.window_resizable = False
    page.padding = 50
    page.window_width = 1024
    page.window_height = 700
    page.window_center()
    
    nome_tabela = ft.TextField(
        label="Nome Tabela",
        width=300,
        border_color='blue',
        border_width=3)
    
    ano = ft.TextField(
        label="Ano Tabela",
        width=300,
        border_color='blue',
        border_width=3)
    
    
    pesquisa = ft.TextField(label="Digite o que deseja pesquisar!",
                            width=300,
                            border_color='blue',
                            border_width=3)
    
    
    enviar_dados = ft.ElevatedButton("Fazer pesquisa",
                                     on_click=lambda _:imprime_dados(),
                                     width=300,
                                     bgcolor='blue',
                                     color='white')
    
    
    salva = ft.ElevatedButton("Salvar em PDF",
                                     on_click=lambda _:salvar_pdf(nome_tabela.value, ano.value,pesquisa.value),
                                     width=300,
                                     bgcolor='blue',
                                     color='white')
    
    centralizar_verticalmente = ft.Column(
        [
            nome_tabela,
            ano,
            pesquisa,
            enviar_dados,
            salva
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        height=500,
        spacing=30
        
    )

    page.add(centralizar_verticalmente)

    page.update()

ft.app(target=main)