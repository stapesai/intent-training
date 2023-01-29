from sklearn.model_selection import StratifiedShuffleSplit
from keras.utils import to_categorical
from training_data._parse_data import get_data
from helper_data._data_augmentation import process_data, no_entity_process_data
from processing._prepare import prepare
from classifiers._classifier import model_def
from controller._saving import save_metadata
from classifiers._validation import Metrics


# start training
def start_train(data):
    entity, train, intent_entity = get_data(data)
    if entity.empty:
        train, entity_extractor = no_entity_process_data(train)
    else:
        train, entity_extractor = process_data(train, entity)
    word_max_length, word_vocab_size, word_Xtrain, ytrain, encoder, word_tokenizer, helper_tokens = prepare(
        train)
    final_model = model_def(word_max_length, word_vocab_size, encoder.classes_)
    save_metadata((intent_entity, entity_extractor, word_tokenizer,
                  encoder, word_max_length, helper_tokens))
    mcc = Metrics()
    sss = StratifiedShuffleSplit(n_splits=5, test_size=0.3)
    print("> Training Intent Model")
    for train_index, test_index in sss.split(word_Xtrain, ytrain):
        X_train, X_test = word_Xtrain[train_index], word_Xtrain[test_index]
        y_train, y_test = to_categorical(
            ytrain[train_index]), to_categorical(ytrain[test_index])
        final_model.fit(X_train, y_train, epochs=20, verbose=0, shuffle=True,
                        validation_data=(X_test, y_test), callbacks=[mcc])
    del final_model

    return
