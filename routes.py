from controllers.productControllers import GetProductsController, SearchProductByIdController, DeleteProductByIdController, PutProductByIdController, PostProductController, PostBuyProductController
from controllers.informationController import MainInformationController, ProductInformationController, AboutInformationController
from controllers.cartControllers import GetCartsController

menu = {
        "1": MainInformationController,
        "1_1": ProductInformationController,
        "1_1_1": GetProductsController,
        "1_1_2": SearchProductByIdController,
        "1_1_3": DeleteProductByIdController,
        "1_1_4": PutProductByIdController,
        "1_1_5": PostProductController,
        "1_2": PostBuyProductController,
        "1_3": GetCartsController,
        "1_99": AboutInformationController,
}