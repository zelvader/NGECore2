import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('twisted_rill')
	mobileTemplate.setLevel(11)
	mobileTemplate.setMinLevel(10)
	mobileTemplate.setMaxLevel(13)
	mobileTemplate.setDifficulty(0)
	mobileTemplate.setAttackRange(5)
	mobileTemplate.setAttackSpeed(1.0)
	mobileTemplate.setWeaponType(6)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Carnivore Meat")
	mobileTemplate.setMeatAmount(35)
	mobileTemplate.setHideType("Bristly Hide")
	mobileTemplate.setBoneAmount(20)	
	mobileTemplate.setBoneType("Animal Bone")
	mobileTemplate.setHideAmount(15)
	mobileTemplate.setSocialGroup("twisted")
	mobileTemplate.setAssistRange(6)
	mobileTemplate.setStalker(False)
	
	templates = Vector()
	templates.add('object/mobile/shared_rill.iff')
	mobileTemplate.setTemplates(templates)

	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', 6, 1.0)
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('twisted_rill', mobileTemplate)
	return