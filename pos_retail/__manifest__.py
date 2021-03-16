# -*- coding: utf-8 -*
# TL Technology (thanhchatvn@gmail.com)
# OPL-1 license
# Not allow resale, editing source codes
# License: Base on Odoo Proprietary License v1.0
{
    "price": "550",
    "name": "POS All-In-One (PRO VERSION)",
    "version": "1.1.4.2",
    "category": "Point of Sale",
    "author": "TL Technology",
    "summary":
        """
        1ST Solution of Point Of Sale \n
        Supported Enterprise and Community \n
        Included 300+ features of POS \n
        Retail & Restaurant Supported \n\
        """,
    "description":
        """
        1ST Solution of Point Of Sale \n
        Supported Enterprise and Community \n
        Included 300+ features of POS \n
        Retail & Restaurant Supported \n\
        """,
    "live_test_url": "http://posodoo.com",
    "website": "http://posodoo.com",
    "sequence": 0,
    "depends": [
        "sale_stock",
        "account",
        "sale_management",
        "hr",
        "bus",
        "stock_account",
        "purchase",
        "product",
        "product_expiry",
        "pos_restaurant",
        "pos_discount",
        "pos_hr",
        "mail",
        "mail_bot",
        "im_livechat",
        "mrp",
        "base_geolocalize",
        "sale_coupon",
        "product_expiry"
    ],
    "demo": ["demo/demo_data.xml"],
    "data": [
        "import_libraries.xml",
        "security/ir.model.access.csv",
        "security/group.xml",
        "security/ir_rule.xml",
        "views/Menu.xml",
        "reports/pos_lot_barcode.xml",
        "reports/pos_sale_analytic.xml",
        "reports/report_pos_order.xml",
        "reports/res_partner_card.xml",
        "reports/pos_sale_report_template.xml",
        "reports/pos_sale_report_view.xml",
        "reports/pos_order_report.xml",
        "reports/pos_voucher_card.xml",
        "reports/restaurant_table_qrcode.xml",
        "reports/coupon.xml",
        "datas/product.xml",
        "datas/schedule.xml",
        "datas/email_template.xml",
        "datas/customer.xml",
        "datas/res_partner_type.xml",
        "datas/barcode_rule.xml",
        "datas/pos_loyalty_category.xml",
        "datas/sequence.xml",
        "views/MrpProduction.xml",
        "views/AccountBankStatement.xml",
        "views/PosConfig.xml",
        "views/PosEpson.xml",
        "views/POSGiftCard.xml",
        "views/PosIot.xml",
        "views/PosSession.xml",
        "views/ProductTemplate.xml",
        "views/ProductVariant.xml",
        "views/ProductBarcode.xml",
        "views/ProductCollege.xml",
        "views/ProductGenericOption.xml",
        "views/ProductModel.xml",
        "views/ProductPricelist.xml",
        "views/ProductSex.xml",
        "views/PosOrder.xml",
        "views/PosOrderLog.xml",
        "views/PosPackOperationLot.xml",
        "views/PosPaymentMethod.xml",
        "views/PosPayment.xml",
        "views/SaleOrder.xml",
        "views/PosLoyalty.xml",
        "views/ResPartnerCredit.xml",
        "views/ResPartnerGroup.xml",
        "views/ResPartnerType.xml",
        "views/ResPartner.xml",
        "views/Restaurant.xml",
        "views/RestaurantPrinter.xml",
        "views/ResUsers.xml",
        "views/PosPromotion.xml",
        "views/AccountJournal.xml",
        "views/AccountMove.xml",
        "views/AccountPayment.xml",
        "views/CouponProgram.xml",
        "views/HrEmployee.xml",
        "views/PosVoucher.xml",
        "views/ProductAddons.xml",
        "views/PosBranch.xml",
        "views/PosBackUpOrder.xml",
        "views/PosTag.xml",
        "views/PosNote.xml",
        "views/PosComboItem.xml",
        "views/StockProductionLot.xml",
        "views/StockQuantQueue.xml",
        "views/StockPicking.xml",
        "views/PosQuicklyPayment.xml",
        "views/PosGlobalDiscount.xml",
        "views/PurchaseOrder.xml",
        "views/PosCallLog.xml",
        "views/PosCategory.xml",
        "views/PosCacheDatabase.xml",
        "views/ProductPackaging.xml",
        "views/PosIot.xml",
        "views/PosSyncSessionLog.xml",
        "views/PosServiceCharge.xml",
        "views/StockInventory.xml",
        "views/StockLocation.xml",
        "views/StockMove.xml",
        "views/StockWarehouse.xml",
        "views/Pax.xml",
        # Wizard
        "wizards/RemovePosOrder.xml",
        "wizards/PosRemoteSession.xml",
        "wizards/PosBox.xml",
    ],
    "qweb": [
        "static/src/xml/Popups/*.xml",
        "static/src/xml/ChromeWidgets/*.xml",
        "static/src/xml/Misc/*.xml",
        "static/src/xml/Screens/AccountMove/*.xml",
        "static/src/xml/Screens/CheckIn/*.xml",
        "static/src/xml/Screens/ProductScreen/ControlButtons/*.xml",
        "static/src/xml/Screens/ProductScreen/CashControl/*.xml",
        "static/src/xml/Screens/ProductScreen/Cart/*.xml",
        "static/src/xml/Screens/ProductScreen/*.xml",
        "static/src/xml/Reports/*.xml",
        "static/src/xml/Screens/Login/*.xml",
        "static/src/xml/Screens/OrderManagementScreen/*.xml",
        "static/src/xml/Screens/ClientList/*.xml",
        "static/src/xml/Screens/GiftCardScreen/*.xml",
        "static/src/xml/Screens/FloorScreen/*.xml",
        "static/src/xml/Screens/Receipt/*.xml",
        "static/src/xml/Screens/Restaurant/ChromeWidgets/*.xml",
        "static/src/xml/Screens/Restaurant/ControlButtons/*.xml",
        "static/src/xml/Screens/Restaurant/FloorScreen/*.xml",
        "static/src/xml/Screens/Restaurant/KitchenScreen/*.xml",
        "static/src/xml/Screens/Restaurant/QrCodeOrderScreen/*.xml",
        "static/src/xml/Screens/Restaurant/Receipt/*.xml",
        "static/src/xml/Screens/Restaurant/RegisterScreen/*.xml",
        "static/src/xml/Screens/Restaurant/SplitBillScreen/*.xml",
        "static/src/xml/Screens/SaleOrder/*.xml",
        "static/src/xml/Screens/PosOrder/*.xml",
        "static/src/xml/Screens/Payment/*.xml",
        "static/src/xml/Screens/reports/*.xml",
        "static/src/xml/Screens/Ticket/*.xml",
        "static/src/xml/Widgets/*.xml",
        "static/src/libs/xml/*.xml",
        "static/src/xml/Themes.xml",
        "static/src/xml/Chrome.xml",

    ],
    "currency": "EUR",
    "installable": True,
    "auto_install": True,
    "application": True,
    "images": ["static/description/icon.png"],
    "support": "thanhchatvn@gmail.com",
    "license": "OPL-1",
    "post_init_hook": "_auto_clean_cache_when_installed",
}
