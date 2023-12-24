#ELEMENTS XPATH FOR LOGIN TEST

ELEMENT_EMAIL = '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]'
ELEMENT_PASSWORD = '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]'
ELEMENT_AUTH_BUTTON_SECOND_SCREEN = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View/android.widget.Button'
ELEMENT_INVALID_AUTH_MESSAGE = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/snackbar_text"]'  #c текстом
ELEMENT_MENU = '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
ELEMENT_AUTH_BUTTON = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button'
ELEMENT_SETTINGS_APP ='//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Настройки приложения"]'
ELEMENT_LOGOUT = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[6]/android.view.View/android.view.View[1]'
ELEMENT_ADD_HUB = '//android.view.ViewGroup[@resource-id="com.ajaxsystems:id/hubAdd"]'
