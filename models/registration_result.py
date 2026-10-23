from dataclasses import dataclass

@dataclass
class RegistrationResult:
    success: bool
    message: str
    student_id: str | None = None