import Link from "next/link"
import Image from "next/image"

const Footer = () => {
	return (
		<>
			<hr className="mt-5" />
			<div className="gap-y-5 w-full py-10 flex flex-col justify-center items-center md:flex-row md:justify-around md:py-20">
				<div className=" flex items-center">
					<Image src="/houseparty.png" alt="favicono" width={48} height={48} />
					<h1 className="font-semibold">Intern assistant</h1>
				</div>

				<div className="">
					<h1 className="font-semibold uppercase">Services</h1>
					<div className="flex gap-x-4">
						<Link
							href="http://13.229.79.190/docs"
							target="_blank"
							className="hover:text-purple-500"
						>
							<p>API</p>
						</Link>
						<Link href="#" target="_blank" className="hover:text-purple-500">
							<p>Document</p>
						</Link>
						<Link href="#" target="_blank" className="hover:text-purple-500">
							<p>Article</p>
						</Link>
						<Link href="#" target="_blank" className="hover:text-purple-500">
							<p>Github</p>
						</Link>
					</div>
				</div>
			</div>
		</>
	)
}

export default Footer
