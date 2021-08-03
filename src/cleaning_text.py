import re
import nltk

nltk.download("wordnet")
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

stopword_list = set(stopwords.words("english"))
import unicodedata
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer


class Text:
    """
    Takes a a list of descriptions as an argument and prepares it for the vectorization by:

    Getting:
        description between quotes
    Removing:
        stopwords,
        accented chars

    Performing:
        perfoming regex tokenization,
        word lemmatizer

    Returning:
        list of strings
    """

    def __init__(self, text: list) -> None:
        self.__text = text

    @property
    def get_text(self) -> list:
        return self.__text

    @staticmethod
    def find_quote(text: str) -> str:
        """
        Finds a description between quotes, otherwise returns whole string
        """

        matches = re.findall(r"\"(.+?)\"", text)
        if len(matches) != 0:
            return ",".join(matches)
        else:
            return text

    @staticmethod
    def remove_stopwords(quote: str, is_lower_case=False) -> str:
        tokenizer = ToktokTokenizer()
        tokens = tokenizer.tokenize(quote)
        tokens = [token.strip() for token in tokens]

        if is_lower_case:
            filtered_tokens = [token for token in tokens if token not in stopword_list]
        else:
            filtered_tokens = [
                token for token in tokens if token.lower() not in stopword_list
            ]
        filtered_text = " ".join(filtered_tokens)

        return filtered_text

    @staticmethod
    def remove_accented_chars(no_stopwords: str) -> str:
        text = (
            unicodedata.normalize("NFKD", no_stopwords)
            .encode("ascii", "ignore")
            .decode("utf-8", "ignore")
        )
        return text

    @staticmethod
    def word_regex_tokenizer(clean_of_accented_chars: str) -> str:
        tokenizer = RegexpTokenizer(r"[a-zA-Z]+")
        token = tokenizer.tokenize(clean_of_accented_chars.lower())
        return " ".join(token)

    @staticmethod
    def word_lemmatizer(regex: str) -> str:
        """
        Examples of lemmatization:

        -> rocks : rock
        -> corpora : corpus
        -> better : good
        """

        lemmatizer = WordNetLemmatizer()
        lem_text = " ".join([lemmatizer.lemmatize(i) for i in regex])
        return lem_text

    def clean_text(self) -> list:
        """
        Perform all static methods in order to clean a string and append it to a list.
        Returns:
            list of strings
        """

        cleaned_entries = []

        for text in self.get_text:
            quote = self.find_quote(text)
            no_stopwords = self.remove_stopwords(quote)
            clean_of_accented_chars = self.remove_accented_chars(no_stopwords)
            regex = self.word_regex_tokenizer(clean_of_accented_chars)
            lemmented = self.word_regex_tokenizer(regex)

            cleaned_entries.extend([lemmented])

        return cleaned_entries
