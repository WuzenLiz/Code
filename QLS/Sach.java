package QLS;

/**
 * Sach
 */
public class Sach extends TaiLieu {

    private String TacGia;
    private int Sotrang;
    private int NamXB;

    public Sach(String Ten_tai_lieu, int Ma_tai_lieu, String nha_XB, int So_ban_PH, int type, String TacGia, int Sotrang, int NamXB) {
        super(Ten_tai_lieu, Ma_tai_lieu, nha_XB, So_ban_PH,type);
        this.TacGia = TacGia;
        this.Sotrang = Sotrang;
        this.NamXB = NamXB;
    }

    public String getTacGia() {
        return this.TacGia;
    }

    public int getSoTrang() {
        return this.Sotrang;
    }

    public int getNamXB() {
        return this.NamXB;
    }

    public void setType() {
        int type = 1;
        this.setType(type);
    }
    
}