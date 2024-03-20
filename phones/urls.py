from django.urls import path, include
from .views import (
    getAllPhones,
    getAllopsys,
    getDetail,
    getAllBrand,
    createBrand,
    createItem,
    createOperationSystem,
    WriteApiView,
)

urlpatterns = [
    path("", getAllPhones),
    path("opSys/", getAllopsys),
    path("brand/", getAllBrand),
    path("<int:id>/", getDetail),
    path("newPhones/", createItem),
    path("newOpSys/", createOperationSystem),
    path("newBrand/", createBrand),
    path("modify/<int:id>/", WriteApiView.as_view()),
]
