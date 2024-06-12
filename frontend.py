import tkinter as tk
from tkinter import ttk
import pandas as pd

# Função para carregar dados do CSV
def load_news(filename='news.csv'):
    df = pd.read_csv(filename)
    return df

# Função para inicializar a interface gráfica
def create_gui(news_df):
    # Cria a janela principal
    root = tk.Tk()
    root.title("News Viewer")

    # Define o tamanho da janela
    root.geometry("800x600")

    # Cria um Treeview para exibir as notícias
    tree = ttk.Treeview(root, columns=('Title', 'Published', 'Source'), show='headings')
    tree.heading('Title', text='Title')
    tree.heading('Published', text='Published')
    tree.heading('Source', text='Source')

    tree.column('Title', width=400)
    tree.column('Published', width=200)
    tree.column('Source', width=100)

    # Adiciona os dados ao Treeview
    for _, row in news_df.iterrows():
        published = str(row['published'])
        tree.insert('', 'end', values=(row['title'], published, row['source']))

    # Adiciona o Treeview à janela
    tree.pack(expand=True, fill='both')

    # Inicia o loop principal da interface gráfica
    root.mainloop()

if __name__ == '__main__':
    # Carrega os dados do CSV
    news_df = load_news()

    # Cria e exibe a interface gráfica
    create_gui(news_df)
