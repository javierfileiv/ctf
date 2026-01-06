i=0
sshpass -p $(cat narnia$i | head -1) ssh narnia$i@narnia.labs.overthewire.org -p 2226

