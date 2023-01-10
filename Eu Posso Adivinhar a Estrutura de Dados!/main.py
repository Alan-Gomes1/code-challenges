try:
  while qtde_casos:= int(input()):
    resposta = []
    eh_fila = eh_pilha = eh_fprioridade = True

    priority_queue = []
    stack = []
    queue = []

    for i in range(qtde_casos):
      acao, valor = map(int, input().split())
      if acao == 1:
        priority_queue.append(valor)
        stack.append(valor)
        queue.append(valor)
      elif acao == 2:
        # Fila de prioridade
        if sorted(priority_queue, reverse=True)[0] != valor:
          eh_fprioridade = False
        else:
          priority_queue.remove(valor)
        # Fila
        if queue[0] != valor:
          eh_fila = False
        else:
          queue.remove(valor)
        # Pilha
        if stack[-1] != valor:
          eh_pilha = False
        else:
          stack.remove(valor)

    if (not eh_fprioridade ) and (not eh_fila) and (not eh_pilha): # Caso não atenda a nenhuma estrutura
      print("impossible") 
    elif (eh_fprioridade and eh_fila) or (eh_pilha and eh_fila) or (eh_fprioridade and eh_pilha): # Caso atenda a mais de uma estrutura
      print("not sure") 
    else: # Caso atenda somente uma estrutura
      print("queue" if eh_fila else "priority queue" if eh_fprioridade else "stack")
except:
  pass