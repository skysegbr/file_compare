# Efetua uma comparação entre dois arquivos grava as linhas repetidas em um arquivo de log

with open('f1.txt', 'r') as file1:
    with open('f2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('line_file_rep.log', 'w') as file_out:

    for line in same:
        file_out.write(line)
