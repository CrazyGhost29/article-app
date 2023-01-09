from summarizer.sbert import SBertSummarizer

class TextSummarizer:

    def __init__(self):

        self.model = SBertSummarizer('distiluse-base-multilingual-cased-v1')

    def summarize_ratio(self, text, ratio):
        if text == "PAYWALL":
            result = "PAYWALL"
        elif text == "REQUEST UNSUCCESSFUL":
            result = "REQUEST UNSUCCESSFUL"
        else:
            result = self.model(text, ratio = ratio)
        return result

    def summarize_sens(self, text, num_sens):
        if text == "PAYWALL":
            result = "PAYWALL"
        elif text == "REQUEST UNSUCCESSFUL":
            result = "REQUEST UNSUCCESSFUL"
        else:
            result = self.model(text, num_sentences = num_sens)
        return result