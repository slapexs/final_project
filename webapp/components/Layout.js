import Footer from "./Footer"
import Navbar from "./Navbar"

import { Prompt } from "@next/font/google"

const fontPrompt = Prompt({ weight: "400", subsets: ["thai"] })

const Layout = ({ children }) => {
	return (
		<>
			<div className={fontPrompt.className}>
				<Navbar />
				{children}
				<Footer />
			</div>
		</>
	)
}

export default Layout
