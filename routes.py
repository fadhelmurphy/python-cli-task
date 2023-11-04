from controllers.productControllers import AllProductsController, ProductByIdController
from controllers.informationController import MainInformationController, ProductInformationController

menu = {
        "1": MainInformationController,
        "1_1": ProductInformationController,
        "1_1_1": AllProductsController,
        "1_1_2": ProductByIdController,
        "1_6": """
About
This application build from scratch by Fadhel Ijlal Falah (Iron Man)
        """,
}