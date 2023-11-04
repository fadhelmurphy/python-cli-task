from controllers.productControllers import AllProductsController, ProductByIdController, DeleteProductByIdController, UpdateProductByIdController, AddProductController
from controllers.informationController import MainInformationController, ProductInformationController

menu = {
        "1": MainInformationController,
        "1_1": ProductInformationController,
        "1_1_1": AllProductsController,
        "1_1_2": ProductByIdController,
        "1_1_3": DeleteProductByIdController,
        "1_1_4": UpdateProductByIdController,
        "1_1_5": AddProductController,
        "1_6": """
About
This application build from scratch by Fadhel Ijlal Falah (Iron Man)
        """,
}