import Head from 'next/head'
import styles from '../styles/Home.module.css'
import '../styles/main.css'

const Logo = () => (
  <>
    <img src="https://image.flaticon.com/icons/svg/18/18333.svg" width={50} className="p-2 hidden md:inline-block" />
  </>
)

const Menu = () => (
  <div className="p-2 flex items-center">
    <a href="https://github.com/udfds" target="_blank">Github</a>
    <a href="https://www.instagram.com/snn.krn" target="_blank">Instagram</a>
    <a href="https://profile.codersrank.io/user/udfds" target="_blank">CodersRank</a>
  </div>
)

const Banner = () => (
  <div className="container max-w-5xl m-auto p-6 flex-1 flex flex-col justify-center items-center sm:items-start text-center sm:text-left">
    <span className="text-gray">Hello world!</span>
    <div className="uppdercaser text-4xl font-extrabold leading-snug new-class">
      <span className="text-deep">SNNKRN</span>
    </div>
    <span className="text-gray">!dlrow olleH</span>
  </div>
)

const Header = () => (
  <div className="flex items-center justify-between flex-wrap bg-teal-500 p-6">
    <Logo />
    <Menu />
  </div>
)

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Tailwindcss Lab</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <Banner />
    </div>
  )
}
