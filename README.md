# dona-yo

Dona Yô é um painel cívico **não oficial** para acompanhar consultas públicas e outras formas de participação popular no Brasil (Congresso, Executivo e Judiciário), com foco em linguagem simples e ordenação por urgência (prazo mais próximo primeiro).

> Não somos um canal oficial do governo. Dona Yô é uma personagem fictícia.

## Estrutura inicial

- `etl/collectors/`
- `etl/processors/`
- `etl/validators/`
- `data/`
- `src/pages/`
- `src/components/`
- `.github/workflows/`

## Regras desta versão de esqueleto

- Sem backend e sem banco de dados.
- Site estático com Astro.
- Dados de exemplo são claramente fictícios.
- Onde faltar fonte real, usar placeholder com `TODO`.

## Como rodar

```bash
npm install
npm run dev
```

Para validar os dados:

```bash
npm run validate:data
```

## Automações (GitHub Actions)

- `coleta_dados.yml`: estrutura de coleta agendada a cada 6 horas (com TODO).
- `verificacao_links.yml`: checa status HTTP dos links e falha com alerta quando encontra link quebrado.
