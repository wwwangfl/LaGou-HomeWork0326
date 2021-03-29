from hero_factory import HeroFactory

hero_factory = HeroFactory()
timo = hero_factory.create_hero("Timo")
police = hero_factory.create_hero("Police")
timo.speak_lines()
police.speak_lines()
police.figth(police.hp, police.power)
