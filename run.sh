
#!/bin/bash
echo "Rodando o código principal..."
python src/Trabalho_Programacao_Funcional.py

echo "Executando testes..."
python -m unittest discover tests
