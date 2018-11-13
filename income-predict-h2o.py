import h2o
from h2o.estimators.random_forest import H2ORandomForestEstimator
from h2o.grid.grid_search import H2OGridSearch


h2o.init()

data = h2o.import_file('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
print(data)

x = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14"]
y = "C15"

data["C1"] = data["C1"].asnumeric()
data["C2"] = data["C2"].asfactor()
data["C3"] = data["C3"].asnumeric()
data["C4"] = data["C4"].asfactor()
data["C5"] = data["C5"].asfactor()
data["C6"] = data["C6"].asfactor()
data["C7"] = data["C7"].asfactor()
data["C8"] = data["C8"].asfactor()
data["C9"] = data["C9"].asfactor()
data["C10"] = data["C10"].asfactor()
data["C11"] = data["C11"].asnumeric()
data["C12"] = data["C12"].asnumeric()
data["C13"] = data["C13"].asnumeric()
data["C14"] = data["C14"].asfactor()
data["C15"] = data["C15"].asfactor()
print(data)

dataset = data.as_data_frame()
train, test = data.split_frame([0.8])
h2o.assign(train, "train_rf")
h2o.assign(test, "test_rf")

# Declare model
m = H2ORandomForestEstimator(
        model_id="income_rf",
        seed=1234,
        ignore_const_cols=True,
        ntrees=100,
        stopping_metric="logloss",
        stopping_rounds=3,
        stopping_tolerance=0.02,
        max_runtime_secs=60,
        nfolds=10
        )

m.train(x, y, train)

performance = m.model_performance(test)

print(performance)

modelfile = m.download_mojo(path="C:\\workspace\\commitconf2018\\output_file\\" + m.model_id, get_genmodel_jar=True)
print("Model saved to " + modelfile)
