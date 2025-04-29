import { Link, Outlet, useLocation } from 'react-router-dom'
import classNames from 'classnames'
import styles from './Layout.module.scss'

export const Layout = () => {

  const { pathname } = useLocation()

  const checkActive = (value: string) => {
    if (pathname == value) {
      return styles.active
    } else {
      return styles.item
    }
  }

  return (
    <div>
      <header className={styles.header}>
        <Link className={classNames(checkActive('/home'))} to={'/home'}>Home</Link>
        <Link className={classNames(checkActive('/sign-up'))} to={'/sign-up'}>Sign-up</Link>
        <Link className={classNames(checkActive('/sign-in'))} to={'/sign-in'}>Sign-in</Link>
      </header>
      <main>
        <Outlet />
      </main>
    </div>
  )
}