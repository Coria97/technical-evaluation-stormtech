from enum import IntEnum, Enum, StrEnum

class PackageStatus(IntEnum):  
  DEPOSIT = 0
  DISTRIBUTION = 1
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]
  
class PackageType(Enum):
  SMALL = 1000
  MEDIUM = 3000
  BIG = 5000
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class ReportStatus(StrEnum):
  BROKEN = 'B'
  FACTORY_FAULT = 'F'
  DELAYED = 'D'
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]
