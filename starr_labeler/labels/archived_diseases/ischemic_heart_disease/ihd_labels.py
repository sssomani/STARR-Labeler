from starr_labeler.labels.extract_labels import *


class ihd_labels(labels_base):
    def __init__(self, config, save_name):
        super().__init__(config, save_name)

    def positive_diagnoses(self, merged):
        merged = merged.loc[
            (merged["ICD10 Code"] >= "I20") & (merged["ICD10 Code"] < "I26")
        ]
        merged = merged[["Patient Id", "Accession Number", "Date", "Imaging_dt"]]
        return merged
