"""Модели OTBot."""

from sqlalchemy import TEXT, BIGINT, String, ForeignKey, LargeBinary, true, false
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy.dialects.sqlite import JSON

from bot.enums import UserRole, ViolationStatus
from bot.db.database import Base


class UserModel(Base):
    """Модель пользователя."""

    telegram_id: Mapped[int] = mapped_column(BIGINT, unique=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    phone_number: Mapped[str | None]

    user_role: Mapped[UserRole] = mapped_column(default=UserRole.USER.name)
    is_approved: Mapped[bool] = mapped_column(default=False, server_default=false())  # одобрен
    is_active: Mapped[bool] = mapped_column(default=True, server_default=true())  # активен
    telegram_data: Mapped[dict | None] = mapped_column(JSON)  # данные из telegram
    user_description: Mapped[str | None]

    responsible_area: Mapped[list["AreaModel"]] = relationship("AreaModel", back_populates="responsible_user")
    violations: Mapped[list["ViolationModel"]] = relationship("ViolationModel", back_populates="detector")

    def __str__(self) -> str:
        """Строковое представление."""
        return self.__class__.__name__ + f"({self.first_name} {self.last_name})"


class ViolationModel(Base):
    """Модель обнаруженных нарушений."""

    detector_id: Mapped[int] = mapped_column(ForeignKey("usermodel.id", name="fk_detector_user_id"))
    detector: Mapped["UserModel"] = relationship("UserModel", back_populates="violations")

    area_id: Mapped[int] = mapped_column(ForeignKey("areamodel.id", name="fk_violation_area_id"))
    area: Mapped["AreaModel"] = relationship("AreaModel", back_populates="violations")

    picture: Mapped[bytes] = mapped_column(LargeBinary)
    description: Mapped[str] = mapped_column(String(200))
    status: Mapped[ViolationStatus] = mapped_column(default=ViolationStatus.ACTIVE)
    category: Mapped[str]
    actions_needed: Mapped[str] = mapped_column(TEXT)  # Мероприятия по устранению нарушения

    def __str__(self) -> str:
        """Строковое представление."""
        return self.__class__.__name__ + f"({self.description})"


class AreaModel(Base):
    """Модель места нарушения."""

    name: Mapped[str] = mapped_column(unique=True, info={"verbose_name": "Имя места"})
    description: Mapped[str | None] = mapped_column(info={"verbose_name": "Описание места"})
    violations: Mapped[list["ViolationModel"]] = relationship("ViolationModel", back_populates="area")

    responsible_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("usermodel.id", name="fk_area_responsible_user_id"),
        info={"verbose_name": "Ответственный из зарегистрированных"})
    responsible_user: Mapped["UserModel"] = relationship("UserModel", back_populates="responsible_area")
    # Поле для ручного ввода ФИО ответственного
    responsible_text: Mapped[str | None] = mapped_column(
        String(250),
        info={"verbose_name": "Ответственный введённый вручную"})

    def __str__(self) -> str:
        """Строковое представление."""
        return self.__class__.__name__ + f"({self.name})"

