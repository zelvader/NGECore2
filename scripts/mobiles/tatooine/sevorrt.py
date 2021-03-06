import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('sevorrt')
	mobileTemplate.setLevel(5)
	mobileTemplate.setMinLevel(4)
	mobileTemplate.setMaxLevel(6)
	mobileTemplate.setDifficulty(0)
	mobileTemplate.setAttackRange(5)
	mobileTemplate.setAttackSpeed(1.0)
	mobileTemplate.setWeaponType(6)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Reptilian Meat")
	mobileTemplate.setMeatAmount(10)
	mobileTemplate.setHideType("Leathery Hide")
	mobileTemplate.setBoneAmount(10)	
	mobileTemplate.setBoneType("Animal Bone")
	mobileTemplate.setHideAmount(4)
	mobileTemplate.setSocialGroup("sevorrt")
	mobileTemplate.setAssistRange(0)
	mobileTemplate.setStalker(False)	
	
	templates = Vector()
	templates.add('object/mobile/shared_sevorrt.iff')
	mobileTemplate.setTemplates(templates)

	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', 6, 1.0)
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('sevorrt', mobileTemplate)
	return