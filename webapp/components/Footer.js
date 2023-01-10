import Link from "next/link"

const Footer = () => {
	return (
		<>
			<hr />
			<div className="bg-white sm:py-20 lg:20 justify-center flex">
				<div className="w-3/4">
					<div className="flex flex-row items-center justify-between">
						<div className="flex items-center">
							<img src="./houseparty.png" className="w-12" />
							<h1 className="font-bold">
								Intern <br /> assistant
							</h1>
						</div>

						<div>
							<h1 className="font-bold uppercase">Service</h1>
							<div className="flex flex-row gap-x-10 mt-3 text-gray-500">
								<p>API</p>
								<p>Github</p>
								<p>Document</p>
								<p>Article</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</>
	)
}

export default Footer
