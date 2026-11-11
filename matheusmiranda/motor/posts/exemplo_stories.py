"""Exemplo de stories: frase escura, print no celular e capa de post. Rode: python3 posts/exemplo_stories.py"""
import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from story import render
import marca
S = RAIZ + '/saida'
PE = f'post novo no perfil · @{marca.HANDLE}'
WA = 'chama no whatsapp · link no perfil'
L = [
 dict(nome='s01-frase', escuro=True, olho='Rótulo', titulo='Frase curta. <em>A virada em destaque.</em>', t=100, sub='Uma linha de apoio. <b>O ponto forte.</b>', pe=WA),
 dict(nome='s02-celular', olho='Rótulo', titulo='O produto <em>no celular.</em>', t=92, cel='adv2-cel-capa.png', pe=WA),
 dict(nome='s03-capa', olho='Rótulo', titulo='Chamada pro <em>post do dia.</em>', t=90, capa=f'{S}/exemplo-formatos/01.png', pe=PE),
]
render(L, f'{S}/stories-exemplo')
