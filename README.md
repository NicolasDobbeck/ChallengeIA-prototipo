# Descrição do Projeto

No dinâmico cenário da mobilidade urbana, a gestão de grandes frotas como a da Mottu enfrenta desafios significativos. A ausência de um sistema centralizado e em tempo real para monitorar veículos resulta em perdas de tempo na localização de motos, ineficiência operacional, elevação de custos e decisões prejudicadas pela falta de dados precisos. Nós identificamos essa lacuna e desenvolvemos uma solução inovadora para revolucionar o mapeamento geográfico e o rastreamento em tempo real da sua frota de motos.<br><br>
Nossa solução oferece uma visão clara e dinâmica da distribuição e do status de cada veículo. Imagine ter um mapa interativo onde cada pátio é uma área delimitada e, dentro dela, marcadores visuais indicam a localização exata de cada moto, esteja ela parada ou em movimento. Essa funcionalidade proporciona um rastreamento em tempo real que permite a qualquer operador identificar instantaneamente a moto e sua posição, além de acessar informações cruciais como seu status operacional: se está disponível, em uso, em manutenção ou aguardando retirada. Isso não só facilita o gerenciamento da frota, mas empodera a equipe a visualizar rapidamente a quantidade de motos em cada local, promovendo uma gestão mais proativa e estratégica.<br><br>
A implementação deste sistema representa um avanço significativo para a Mottu, trazendo benefícios tangíveis que impactam diretamente a eficiência e a economia da operação. A eficiência operacional é aprimorada substancialmente, pois o acesso rápido à localização e ao status das motos elimina a necessidade de buscas manuais, agilizando processos como a retirada de veículos e a organização de manutenções. Isso se traduz em uma redução de custos notável, otimizando recursos e respondendo dinamicamente às demandas do mercado.<br><br>
Este projeto vai muito além de um simples sistema de rastreamento; ele é um passo fundamental na evolução da gestão de frotas da Mottu. Ao oferecer uma visão clara e em tempo real de seus ativos, nossa solução capacita a empresa a operar com uma eficiência sem precedentes. Acreditamos que essa capacidade de monitoramento inteligente não só aprimora as operações diárias, mas também abre portas para inovações futuras, contribuindo significativamente para um cenário de mobilidade urbana mais conectado, seguro e eficiente. Com este projeto, a Mottu está pavimentando o caminho para um futuro onde a logística de frotas é mais inteligente e responsiva.

## Tecnologias e Frameworks:

Python: Linguagem de programação principal utilizada em todo o notebook para manipulação de dados, pré-processamento de texto, e aplicação de modelos de Machine Learning.
<br><br>
Google Colab: Ambiente de desenvolvimento baseado em nuvem que permite a execução de notebooks Jupyter. É utilizado para montar o Google Drive, instalar bibliotecas, e gerenciar arquivos.
<br><br>
Pandas: Biblioteca Python para manipulação e análise de dados. É amplamente utilizada para carregar o dataset CSV em um DataFrame, visualizar as primeiras linhas, obter informações sobre as colunas, e adicionar novas colunas.<br><br>
scikit-learn (sklearn): Biblioteca Python para Machine Learning. Diversas funcionalidades do scikit-learn são empregadas:
- TfidfVectorizer: Para vetorização de texto.
- cosine_similarity: Para cálculo de similaridade.
- KMeans: Para agrupamento de dados.

Joblib: Biblioteca Python para serialização e desserialização de objetos Python. É utilizada para salvar o TfidfVectorizer treinado em um arquivo .joblib para uso posterior.
<br><br>
Kaggle API: Utilizada para baixar o dataset "motorcycle-dataset" diretamente do Kaggle para o ambiente Colab.

## Técnicas e Algoritmos Utilizados e Justificados:
### Montagem do Google Drive e Configuração do Kaggle:
- Técnica: Montagem do Google Drive (drive.mount('/content/drive')) e configuração da API do Kaggle (criação de diretório ~/.kaggle, cópia do arquivo kaggle.json, e ajuste de permissões).
- Justificativa: Essencial para acessar o arquivo kaggle.json armazenado no Google Drive para autenticação com a API do Kaggle e para baixar o dataset necessário para o projeto.

### Pré-processamento de Dados:

- Técnica: Leitura de arquivo CSV (pd.read_csv()), inspeção inicial dos dados (df.head(), df.info()), e limpeza de texto (preprocess_text usando re.sub()).
- Justificativa: A leitura do CSV é o primeiro passo para carregar os dados. A inspeção ajuda a entender a estrutura e os tipos de dados, identificando colunas como ex_showroom_price com valores nulos. O pré-processamento do nome das motos, removendo caracteres especiais e convertendo para minúsculas, é crucial para padronizar o texto e garantir que a vetorização de texto e o cálculo de similaridade funcionem corretamente, tratando "Royal Enfield" e "royal enfield" como o mesmo termo.

### Vetorização de Texto (TF-IDF):

- Técnica: TfidfVectorizer.
Algoritmo/Conceito: TF-IDF (Term Frequency-Inverse Document Frequency). Este algoritmo atribui pesos às palavras com base na sua frequência em um documento e na sua raridade em todo o corpus de documentos.
- Justificativa: O TF-IDF é utilizado para converter os nomes textuais das motos em representações numéricas (vetores) que podem ser compreendidas por algoritmos de Machine Learning. Isso é fundamental para calcular a similaridade entre os nomes das motos, pois palavras mais discriminativas (aquelas que aparecem em poucos nomes, mas são importantes para diferenciá-los) terão pesos maiores.

### Cálculo de Similaridade (Similaridade de Cosseno):

- Técnica: cosine_similarity.
- Algoritmo/Conceito: Similaridade de Cosseno. Mede o cosseno do ângulo entre dois vetores não nulos no espaço multidimensional. Quanto mais próximos de 1 os vetores estiverem, mais similares são.
Justificativa: A similaridade de cosseno é escolhida para determinar quão semanticamente semelhantes são os nomes das motos. Ao invés de usar a distância euclidiana, que é sensível à magnitude dos vetores, a similaridade de cosseno foca na orientação, sendo mais adequada para dados esparsos como os gerados pelo TF-IDF e para capturar a semelhança temática entre os nomes das motos.

### Sistema de Recomendação (Baseado em Similaridade de Item):

- Técnica: get_similar_bikes.
Algoritmo/Conceito: Recomendação baseada em conteúdo/item-item.
- Justificativa: Uma vez que a matriz de similaridade de cosseno é calculada, é possível encontrar motos semelhantes a uma dada moto. O sistema retorna as motos com os maiores scores de similaridade, excluindo a própria moto de consulta. Isso permite ao usuário descobrir motos com nomes ou características textuais semelhantes, que podem indicar modelos, marcas ou estilos parecidos.

### Agrupamento (K-Means):

- Técnica: KMeans.
Algoritmo/Conceito: K-Means Clustering. Um algoritmo de agrupamento que particiona n observações em k clusters, onde cada observação pertence ao cluster cujo centroide é o mais próximo.
- Justificativa: O K-Means é aplicado aos vetores TF-IDF para agrupar motos com nomes semelhantes em clusters. Isso pode ser útil para identificar categorias de motos com base em seus nomes, sem a necessidade de rótulos pré-definidos. Por exemplo, motos da mesma marca ou série podem acabar no mesmo cluster, o que pode ser explorado para análise ou para criar recomendações baseadas em clusters.

### Persistência de Modelo:

- Técnica: Serialização com joblib.dump().
- Justificativa: Salvar o TfidfVectorizer treinado é crucial para que ele possa ser reutilizado posteriormente sem a necessidade de retreiná-lo. Em um ambiente de produção, isso economiza tempo e recursos computacionais, garantindo que novas consultas de similaridade ou agrupamento usem a mesma lógica de vetorização utilizada no treinamento.



