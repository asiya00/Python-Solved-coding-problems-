public class hack1
{
	public static void main(String[] args) {
		hack2 h = new hack2();
		System.out.println(h.H);
		h.hack_method();	
	}
}

class hack2{
	protected int H = 1;

	void hack_method()
	{
		System.out.println(H);
	}
}

// 1
// 1