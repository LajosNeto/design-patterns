package creational.abstractFactory.equipments

interface Armor {
    fun displayName(): String
    fun defend(attackValue: Int): Int
}