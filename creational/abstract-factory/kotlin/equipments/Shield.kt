package creational.abstractFactory.equipments

interface Shield {
    fun displayName(): String
    fun block(attackValue: Int): Int
}