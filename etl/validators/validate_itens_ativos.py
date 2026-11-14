#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def validar_item(item: dict, index: int) -> list[str]:
    erros = []
    if not str(item.get("fonte", "")).strip():
        erros.append(f"item[{index}] sem fonte")
    if not str(item.get("prazo_final", "")).strip():
        erros.append(f"item[{index}] sem prazo_final")
    if not str(item.get("rotulo_certeza", "")).strip():
        erros.append(f"item[{index}] sem rotulo_certeza")
    return erros


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: validate_itens_ativos.py <arquivo_json>")
        return 2

    caminho = Path(sys.argv[1])
    if not caminho.exists():
        print(f"Arquivo não encontrado: {caminho}")
        return 2

    dados = json.loads(caminho.read_text(encoding="utf-8"))
    if not isinstance(dados, list):
        print("Formato inválido: esperado array de itens")
        return 1

    erros = []
    for i, item in enumerate(dados):
        if not isinstance(item, dict):
            erros.append(f"item[{i}] não é objeto")
            continue
        erros.extend(validar_item(item, i))

    if erros:
        for erro in erros:
            print(f"ERRO: {erro}")
        return 1

    print("Validação concluída: sem erros")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
