import tkinter as tk
from tkinter import messagebox
import csv # Biblioteca para salvar em formato de planilha

def salvar_voto():
    nome = entry_nome.get()
    ano = entry_ano.get()
    partido = lista_partidos.get(tk.ACTIVE)

    # Validação básica
    if nome == "" or ano == "":
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
        return

    try:
        idade = 2025 - int(ano)
        if idade < 18:
            messagebox.showerror("Negado", f"Cidadão com {idade} anos não pode votar!")
        else:
            # SALVANDO NO ARQUIVO (O Banco de Dados)
            with open('votos_registrados.csv', mode='a', newline='', encoding='utf-8') as ficheiro:
                escritor = csv.writer(ficheiro)
                escritor.writerow([nome, idade, partido])
            
            messagebox.showinfo("Sucesso", f"Voto de {nome} para o {partido} registrado!")
            # Limpa os campos para o próximo
            entry_nome.delete(0, tk.END)
            entry_ano.delete(0, tk.END)
            
    except ValueError:
        messagebox.showerror("Erro", "No campo ano, digite apenas números!")

# --- CRIAÇÃO DA INTERFACE ---
janela = tk.Tk()
janela.title("CNE - Sistema de Votação")
janela.geometry("400x450")

# Estética básica
tk.Label(janela, text="SISTEMA DE VOTO", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(janela, text="Nome do Cidadão:").pack()
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack(pady=5)

tk.Label(janela, text="Ano de Nascimento:").pack()
entry_ano = tk.Entry(janela, width=10)
entry_ano.pack(pady=5)

tk.Label(janela, text="Selecione o Partido:").pack()
lista_partidos = tk.Listbox(janela, height=5)
for p in ["MPLA", "UNITA", "CASA-CE", "PRS", "FNLA"]:
    lista_partidos.insert(tk.END, p)
lista_partidos.pack(pady=10)

btn_votar = tk.Button(janela, text="CONFIRMAR VOTO", bg="green", fg="white", command=salvar_voto)
btn_votar.pack(pady=20)

janela.mainloop()

