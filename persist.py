import utils


class PicklePersistor:
    def __init__(self):
        pass

    def save_index(self, index_df, index_name):
        print(self.__class__.__name__)
        file_name = index_name + ".p"
        utils.pickle_file(index_df, file_name)

    def load_index(self, index_name):
        print(self.__class__.__name__)
        file_name = index_name + ".p"
        return utils.read_pickle(file_name)

    def save_portfolio(self, portfolio,index_name):
        print(self.__class__.__name__)
        portfolio_name = "portfolio-analysis-" + index_name + ".p"
        utils.pickle_file(portfolio, portfolio_name)
        pass

    def load_portfolio(self, portfolio):
        pass

    def save_analysis(self, analysis_df,index_name):
        print(self.__class__.__name__)
        analysis_filename = "analysis-" + index_name + ".p"
        utils.pickle_file(analysis_df, analysis_filename)

    def load_analysis(self, index_name):
        print(self.__class__.__name__)
        analysis_filename = "analysis-" + index_name + ".p"
        return utils.read_pickle(analysis_filename)


class DbPersistor:
    def __init__(self, path):
        self.path = path

    def save_portfolio(self, portfolio):
        pass

    def load_portfolio(self, portfolio):
        pass

    def save_analysis(self, analysis):
        pass

    def load_analysis(self, analysis):
        pass