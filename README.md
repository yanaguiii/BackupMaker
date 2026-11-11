# BackupMaker

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Automação](https://img.shields.io/badge/Automação-Script-161b22?style=flat-square)

Script em Python que cria **backups versionados por data e hora** de qualquer pasta, escolhida por uma janela gráfica. Nunca mais perca um arquivo :)

## Como funciona

1. Abre uma janela (Tkinter) para você escolher a pasta.
2. Cria uma subpasta `backup/` dentro dela, se ainda não existir.
3. Copia todos os arquivos e subpastas para `backup/AAAA-MM-DD HHMM/`, mantendo os metadados (`shutil.copy2` e `shutil.copytree`).
4. Ignora a própria pasta `backup/`, para não copiar backups anteriores.

```text
minha-pasta/
├── relatorio.xlsx
├── fotos/
└── backup/
    ├── 2024-12-10 0930/
    └── 2024-12-11 1815/
        ├── relatorio.xlsx
        └── fotos/
```

## Como executar

Requer **Python 3**. Usa só a biblioteca padrão (`os`, `shutil`, `datetime`, `tkinter`).

```bash
python CriadorBackup.py
```

## Tecnologias

`Python` · `Tkinter` · `shutil` · `os`
