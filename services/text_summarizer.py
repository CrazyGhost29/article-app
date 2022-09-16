from summarizer.sbert import SBertSummarizer
summarizer_model = SBertSummarizer('distiluse-base-multilingual-cased-v1')


class TextSummarizer:

    def __init__(self):

        self.model = SBertSummarizer('distiluse-base-multilingual-cased-v1')

    def summarize_ratio(self, text, ratio):
        result = self.model(text, ratio = ratio)
        return result

    def summarize_sens(self, text, num_sens):
        result = self.model(text, num_sentences = num_sens)
        return result