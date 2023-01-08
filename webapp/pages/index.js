import Head from "next/head"
import Image from "next/image"
import { Prompt } from "@next/font/google"
import styles from "../styles/Home.module.css"

const fontPrompt = Prompt({ weight: "400", subsets: ["thai", "latin"] })

export default function Home() {
	return (
		<>
			<Head>
				<title>
					ระบบแนะนำบริษัทสำหรับฝึกงานตามความสนวจ ด้วยเทตโนโลยีปัญญาประดิษฐ์
				</title>
				<meta
					name="description"
					content="ระบบแนะนำบริษัทสำหรับฝึกงานตามความสนวจ ด้วยเทตโนโลยีปัญญาประดิษฐ์ | Recommended System of Internship's Company"
				/>
				<meta name="viewport" content="width=device-width, initial-scale=1" />
				<link rel="icon" href="/houseparty.png" />
			</Head>

			<h1 className={fontPrompt.className}>สวัสดี</h1>
		</>
	)
}
