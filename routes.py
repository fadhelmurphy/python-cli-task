from controllers.productControllers import GetProductsController, SearchProductByIdController, DeleteProductByIdController, PutProductByIdController, PostProductController, PostBuyProductController
from controllers.informationController import MainInformationController, ProductInformationController, AboutInformationController, GetProductsInformationController
from controllers.cartControllers import GetCartsController, PostCartsCheckoutController

menu = {
        "1": MainInformationController,
        "1_1": ProductInformationController,
        "1_1_1": GetProductsInformationController,
        "1_1_1_1": GetProductsController,
        "1_1_1_2": SearchProductByIdController,
        "1_1_2": DeleteProductByIdController,
        "1_1_3": PutProductByIdController,
        "1_1_4": PostProductController,
        "1_2": PostBuyProductController,
        "1_3": GetCartsController,
        "1_4": PostCartsCheckoutController,
        "1_99": AboutInformationController,
}