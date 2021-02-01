for i in `ls *.json`; do 
  cat $i| tr -d '\n' | tr -d '\r'; echo;
done > /cygdrive/c/Users/hariu/PycharmProjects/tosdr/jsons/amazon.json
