from controllers.productControllers import AllProductsController, ProductByIdController
from controllers.informationController import MainInformation, ProductInformation

menu = {
        "1_1_1": AllProductsController,
        "1_1_2": ProductByIdController,
        "1_6": """
About
This application build from scratch by Fadhel Ijlal Falah (Iron Man)
        """,
}
menu["1"] = MainInformation
menu["1_1"] = ProductInformation