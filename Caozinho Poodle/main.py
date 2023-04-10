while True:
  try:
    documentos, resultados = input().split()
    documentos = int(documentos)
    resultados = int(resultados)

    if documentos == 0:
      break
    paginas = documentos / resultados

    if paginas != int(documentos / resultados):
      paginas = int(paginas) + 1
    else:
      paginas = int(paginas)
      
    if paginas > 6:
      print(end='P')
      if paginas > 20:
        paginas = 20
      for i in range(paginas - 4):
        print(end='o')
      print("dle")

    else:
      print("Poodle")

  except:
    break