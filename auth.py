import pyotp
import qrcode

from config import load_config
cfg = load_config()


def generate_otp_qr_code(user: str) -> str:
    totp = pyotp.TOTP(cfg["otp_code"])

    provisioning_url = totp.provisioning_uri(user, issuer_name="LFDM_DISCORD")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(provisioning_url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_code_filename = "qr_code/authenticator_qr_{}.png".format(user)
    qr_img.save(qr_code_filename)
    return qr_code_filename


def verif_otp_code(code: str) -> bool:
    totp = pyotp.TOTP(cfg["otp_code"])

    verification_code = code

    if totp.verify(verification_code):
        return True
    return False
