from logging import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        """
        This class shall be used for model evaluation pipeline.

        __init__ is the constructor method of class.
        """
        pass

    def main(self):
        """
        This method executes the main model evaluation pipeline process.

        It orchestrates the model evaluation tasks to evaluate the model
        using the data prepared in the previous stages.
        """
        pass




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

